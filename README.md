# employees-service

Demo employees REST service using `miketrout/natural-service-base` as the parent image.

The service is based on Python and Flask and it runs Software AG Natural code to list and get records from the demo EMPLOYEES database.

There are currently two operations:

`GET /s={start}&n={number}`

A list of {number} EMPLOYEE records is returned, sorted by PERSONNEL-ID and starting at record number {start}. For example, with s=1 and n=1:

```JSON
{
    "employees":[
        {
            "personnelId":"11100102",
            "firstName":"EDGAR",
            "middleName":"PETER",
            "lastname":"SCHINDLER"
        }
    ]
}
```

`GET /{personnelId}`

Return the details for the record specified by {personnelId}. For example, using the personnelId returned above:

```JSON
{
    "employee":{
        "personnelId":"11100102",
        "gender":"M",
        "dateOfBirth":"1962-12-04",
        "addressLine1":"BUCHENLANDWEG 84",
        "addressLine2":"6148 HEPPENHEIM"
    }
}
```

To build the service locally, run:

`docker build --tag employees-service .`

To run the service locally:

```sh
docker run -d -e ACCEPT_EULA=Y -e ADADBID=12 -e "ADA_DB_CREATION=demodb" --name adabas-db store/softwareag adabas-ce:6.7.0
docker run -d -p 80:80 --name employees-service employees-service
```

You must have 'bought' (they are free) the `softwareag/adabas-ce` and `softwareag/natural-ce` images from the [Docker Hub Software AG Store](https://hub.docker.com/publishers/softwareag) and accepted the licence agreements. You must `docker login` as the account under which you purchased the `softwareag/adabas-db` image.