## Endpoints
#### Client
- show menu: `jarvis/v1/user/menu/{item_type}`
  - [x] Retrieves all items by type 
- add item to cart: `jarvis/v1/user/add`
  - takes a body payload which is alcohol
- checkout cart: `jarvis/v1/user/checkout`

#### Admin
- add item to db: `jarvis/v1/admin/add/{drink_type}`
  - Body payload `{"name": "Shocktop", "price" : 10.00, "quantity": 10}`
  - [x] Ability to add all alcohol beverage types
  - [x] Ability to specify quantity 
  - [x] Ability to specify price of item 

- update item in db: `jarvis/v1/admin/update/{drink_type}`

#### Run Book for Starting NGROK 
1. `make up`
2. `make logs`
3. ngrok http 8000


