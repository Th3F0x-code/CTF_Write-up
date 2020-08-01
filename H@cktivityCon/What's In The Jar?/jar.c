#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ADD_JAR 1
#define REMOVE_JAR 2
#define VIEW_JARS 3
#define MODIFY_JAR 4
#define START_GAME 5
#define SET_ANSWER 6

typedef struct _answer {
  void(*action)(const char*);
  char* jar;
} answer_t;

const char* g_jar =   \
      "      _____\n" \
      "     `.___,'\n" \
      "      (___)\n" \
      "      <   >\n" \
      "       ) (\n" \
      "      /`-.\\\n" \
      "     /     \\\n" \
      "    / _    _\\\n" \
      "   :,' `-.' `:\n" \
      "   |         |\n" \
      "   :         ;\n" \
      "    \\       /\n" \
      "     `.___.'";

void do_win( const char* contents )
{
  printf("Congratulations! You won %s\n", contents);
}

void do_lose( const char* contents )
{
  printf("Sorry, you lost. As a consolation, you can have %s\n", contents);
}

int main(int argc, char * argv[]) {
  unsigned int njars = 0;
  char* jars[64];
  char format_string[] = "Jar Contents: %s";
  char buffer[32];
  int choice;
  answer_t* correct_answer;

  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);

  puts(g_jar);
  puts("\nFill your jars, then start the game and " \
       "see if your friends can guess where the prize is!");

  while ( 1 ) {
    printf("Main Menu:\n1. Add a jar\n2. Remove Jar\n3. View Jars\n4. Modify Jar\n5. Start Game\n6. Set Answer\n");

    choice = -1;
    while ( choice < 1 || choice > 6 ) {
      puts("Choice: ");
      fgets(buffer, 40, stdin);
      choice = atoi(buffer);
    }

    switch(choice)
    {
      case ADD_JAR:

        // Ensure we have room
        if( njars >= 64 ){
          puts("No more room for jars :(");
          continue;
        }

        // Create a new jar
        jars[njars] = malloc(0xf8);

        // Read in the new contents
        printf("Jar Contents: ");
        fgets(jars[njars], 0xf9, stdin);

        // Increment the pointer
        njars++;
        break;
      case REMOVE_JAR:
        puts("Which Jar? ");
        fgets(buffer, 32, stdin);
        choice = atoi(buffer);
        if( choice < 0 || choice >= njars || jars[choice] == NULL ) {
          puts("Invalid jar!");
        } else {
          free(jars[choice]);
          jars[choice] = NULL;
        }
        break;
      case VIEW_JARS:
        // Show the
        for(int i = 0; i < njars; i++){
          printf(format_string, jars[i]);
        }
        break;
      case MODIFY_JAR:
        puts("Which Jar? ");
        fgets(buffer, 32, stdin);
        choice = atoi(buffer);
        if( choice < 0 || choice >= njars || jars[choice] == NULL ) {
          puts("Invalid jar!");
        } else {
          puts("Jar Contents: ");
          fgets(jars[choice], 0xf9, stdin);
        }
        break;
      case SET_ANSWER:
        // Allocate the answer structure
        correct_answer = malloc(0x100);

        puts("Which jar should win? ");
        fgets(buffer, 32, stdin);
        choice = atoi(buffer);
        if ( choice < 0 || choice >= njars || jars[choice] == NULL ) {
          puts("Invalid jar!");
          break;
        }

        // Fill the answer structure
        correct_answer->action = do_win;
        correct_answer->jar = jars[choice];

        printf("Answer: %p", correct_answer);

        break;

      case START_GAME:
        // Clear the screen
        printf("\x1B[1J");

        printf("Which jar do you think has the prize? (%d-%d)\n", 0, njars-1);
        fgets(buffer, 32, stdin);
        choice = atoi(buffer);

        if( choice < 0 || choice >= njars || jars[choice] == NULL ){
          puts("Invalid jar!");
          do_lose("Absolutely nothing.");
        } else if ( jars[choice] != correct_answer->jar ) {
          do_lose(jars[choice]);
        } else {
          correct_answer->action(jars[choice]);
        }
        break;
    }
  }

}
