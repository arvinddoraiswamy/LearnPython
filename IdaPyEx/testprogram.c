#include <stdio.h>
#include <stdlib.h>
 
int verify_file(const char *filename) {
  char *buffer = malloc(100);
  char *canonicalized_filename = malloc(100);

  canonicalized_filename = canonicalize_file_name(filename);
  printf("%s\n", canonicalized_filename);

  FILE *fd = fopen(filename, "r");
  if (fd == NULL) {
    printf("File cannot be opened\n");
  }
  else {
    fread(buffer, 2, 100, fd);
    printf("%s\n",buffer);
  }
  return 0;
}

int main(int argc, char *argv[]){
   verify_file(argv[1]);
}
