#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <curl>

double download_speed;
double upload_speed;

size_t write_callback(char *ptr, size_t size, size_t nmemb, void *userdata) {
  double downloaded_bytes = (double)size * nmemb;
  download_speed = downloaded_bytes / (double)elapsed_time;
  return size * nmemb;
}

size_t read_callback(char *ptr, size_t size, size_t nmemb, void *userdata) {
  double uploaded_bytes = (double)size * nmemb;
  upload_speed = uploaded_bytes / (double)elapsed_time;
  return size * nmemb;
}

int main(void) {
  CURL *curl;
  CURLcode res;
  double elapsed_time;
  struct timespec start_time, end_time;
  
  curl_global_init(CURL_GLOBAL_ALL);
  curl = curl_easy_init();
  
  if(curl) {
    curl_easy_setopt(curl, CURLOPT_URL, "http://speedtest.net/");
    
    /* Measure download speed */
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, NULL);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
    curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 0L);
    curl_easy_setopt(curl, CURLOPT_PROGRESSFUNCTION, NULL);
    curl_easy_setopt(curl, CURLOPT_HEADER, 0L);
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    
    /* Measure upload speed */
    curl_easy_setopt(curl, CURLOPT_READDATA, NULL);
    curl_easy_setopt(curl, CURLOPT_READFUNCTION, read_callback);
    curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
    
    /* Start timer */
    clock_gettime(CLOCK_MONOTONIC, &start_time);
    
    /* Perform speedtest */
    res = curl_easy_perform(curl);
    
    /* Stop timer */
    clock_gettime(CLOCK_MONOTONIC, &end_time);
    elapsed_time = ((double)end_time.tv_sec + 1.0e-9 * end_time.tv_nsec) - ((double)start_time.tv_sec + 1.0e-9 * start_time.tv_nsec);
    
    /* Check for errors */
    if(res != CURLE_OK) {
      fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
    }
    else {
      printf("Download speed: %.2f MB/s\n", download_speed / 1024.0 / 1024.0);
      printf("Upload speed: %.2f MB/s\n", upload_speed / 1024.0 / 1024.0);
    }
    
    curl_easy_cleanup(curl);
  }
  
  curl_global_cleanup();
  
  return 0;
}
