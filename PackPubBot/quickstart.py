from httplib2 import Http
from json import dumps
import acquire_book

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    #TESTING
    url = 'https://chat.googleapis.com/v1/spaces/AAAASe69zlE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=c9VnTquar3jQwi5VWeMwGrEEi4a5VAq_q_b727PZiZo%3D'
    #REAL
    # url ='https://chat.googleapis.com/v1/spaces/AAAA0YtEOWk/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=MJgYpqLF8-RevMOLouMNu_putwoosFKRGApz96_aKgI%3D'
    bot_message = {'text' : acquire_book.book,
  "cards": [
    {
      "sections": [
        {
          "widgets": [
            {
              "image": {"imageUrl": acquire_book.free_book_image_url, "onClick": { "openLink": {"url": acquire_book.url}}}
            },
            {
              "buttons": [
                {
                  "textButton":{
                    "text": acquire_book.book_text,
                    "onClick": {
                      "openLink":{
                        "url": acquire_book.url
                      }
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
     

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    #print(response)

if __name__ == '__main__':
    main()
