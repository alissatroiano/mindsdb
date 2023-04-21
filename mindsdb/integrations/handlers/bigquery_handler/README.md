# BigQuery Handler

This is the implementation of the BigQuery handler for MindsDB.

## Google BigQuery

BigQuery is a fully-managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is a Platform as a Service that supports querying using ANSI SQL. For more info check https://cloud.google.com/bigquery/.

## Implementation

This handler was implemented using the python `google-cloud-bigquery` library.

The required arguments to establish a connection are:

* `project_id`:  A globally unique identifier for your project
* `service_account_keys`: Full path to the service account key file

For more info about creating and managing the service account key visit  https://cloud.google.com/iam/docs/creating-managing-service-account-keys.

## Usage
### CREATE DATABASE 

In order to make use of this handler and connect to a BigQuery use the following syntax:

```sql
CREATE DATABASE bqdataset
WITH ENGINE = "bigquery",
PARAMETERS = {
   "project_id": "tough-future-332513",
   "service_account_keys": "/home/user/MyProjects/tough-future-332513.json"
   }
```
### Presigned URL 
Alternatively, you can generate a presigned URL for an object using the [S3 console](https://console.aws.amazon.com/s3/) or [AWS Explorer for Visual Studio Code](https://aws.amazon.com/visualstudiocode/). When you generate a presigned URL, make sure that the parameters in your request match the signature exactly.


https://hue-marketplace.s3.us-east-2.amazonaws.com/test.json?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMiJIMEYCIQDEK1sTTyliNnBxZP%2Fsyv1fKc0g1dx1EOJvBfyFdO%2FhkQIhALAbMWqxCTtjBRFk5cuHnKraV5p3FzhNPBek88W49lGbKuwCCMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQAhoMMDAxMTAwNDk3NjM3Igxfqw%2BoVRmF3vfrMT4qwAJKpKfHK%2BTx7XNxMXN4mvB0SM%2BN5V%2BXH0byP4QNlxMpsrpifHjUKX%2BaOKMaNdHS234zAtSS822MsG8jmNQJFf%2BfVAlCDS68O7eCFVojjsyxvcihoUdSJxlh8n9A4KtsOCtzk8lGVxsdqYZcJYvcrN%2FQGNKpEIJ%2FT%2BVvE6nsSJBf89imUToNrmO%2FLKHxUIw1X6HBW4Scau3ZxVmGrmz0FGIR2i84JyohCwdxaDFLauQ4WflwBLKThavDbMCgR0YUhkK8HunCgV9ejazg8esfRya3xCLFllxBCJFUZjtqd%2FWbgoq%2BBkneoGLr95pnzjC6t9rqt3g3G8HGrhS0WqaTlSgLWk7wkZK3LeSEMvxqitL9GoyqIXn3pqyaobX7Fs4V8qWvi50zOagTLxgVeV8%2BWpDN44DiWHdtJ3yfua2TTTwpVTDQ19uhBjqzAu4nKWylinJE57bDzZuviJgRjb37wO4KwfLt8gi9knNUoD6Gp92oQ25cnO3q10MKF5TULZwJFwwMAapk%2Bry%2F0wSQTdprJR%2FXIOiOAscZZ4KmdtOK27k1YqzyfJtqcWFMG7n6Fev9Puc7BU%2Fi7vATGEI%2FYfEzPoGs9NF%2Fu%2F2jTtoS5c6bot5BYjpm2XZ8tCT15X9bBmaMgr3PirIL6%2BFq%2BhxWv1x%2B2uUUZIjkKwE6EdqAowME550uQE9nPhEpxIc%2Fo5bhF6JX5QnECjt4cgPp5Y%2BT%2BKX8fB3BBjncfoYhjMf3YEwjl6SSIY2KxPB%2Bi3OdjIcqV3GSt69aivDnVew92wQdY%2Bt798eO5m9FthhVzkoSSMbNrqoGYbcO10%2FmSXoUIzmkfinSdIlad%2F%2FVZ0beTdv%2F%2BsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230412T173935Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAQAQMYILSVCRYH3RN%2F20230412%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=55f062dabc97694b0052b752750296d7a0e68c6778c2452479ab8cda76754b3e

https://dashuploads.s3.us-east-2.amazonaws.com/0900631B8140782DM.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMiJIMEYCIQDEK1sTTyliNnBxZP%2Fsyv1fKc0g1dx1EOJvBfyFdO%2FhkQIhALAbMWqxCTtjBRFk5cuHnKraV5p3FzhNPBek88W49lGbKuwCCMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQAhoMMDAxMTAwNDk3NjM3Igxfqw%2BoVRmF3vfrMT4qwAJKpKfHK%2BTx7XNxMXN4mvB0SM%2BN5V%2BXH0byP4QNlxMpsrpifHjUKX%2BaOKMaNdHS234zAtSS822MsG8jmNQJFf%2BfVAlCDS68O7eCFVojjsyxvcihoUdSJxlh8n9A4KtsOCtzk8lGVxsdqYZcJYvcrN%2FQGNKpEIJ%2FT%2BVvE6nsSJBf89imUToNrmO%2FLKHxUIw1X6HBW4Scau3ZxVmGrmz0FGIR2i84JyohCwdxaDFLauQ4WflwBLKThavDbMCgR0YUhkK8HunCgV9ejazg8esfRya3xCLFllxBCJFUZjtqd%2FWbgoq%2BBkneoGLr95pnzjC6t9rqt3g3G8HGrhS0WqaTlSgLWk7wkZK3LeSEMvxqitL9GoyqIXn3pqyaobX7Fs4V8qWvi50zOagTLxgVeV8%2BWpDN44DiWHdtJ3yfua2TTTwpVTDQ19uhBjqzAu4nKWylinJE57bDzZuviJgRjb37wO4KwfLt8gi9knNUoD6Gp92oQ25cnO3q10MKF5TULZwJFwwMAapk%2Bry%2F0wSQTdprJR%2FXIOiOAscZZ4KmdtOK27k1YqzyfJtqcWFMG7n6Fev9Puc7BU%2Fi7vATGEI%2FYfEzPoGs9NF%2Fu%2F2jTtoS5c6bot5BYjpm2XZ8tCT15X9bBmaMgr3PirIL6%2BFq%2BhxWv1x%2B2uUUZIjkKwE6EdqAowME550uQE9nPhEpxIc%2Fo5bhF6JX5QnECjt4cgPp5Y%2BT%2BKX8fB3BBjncfoYhjMf3YEwjl6SSIY2KxPB%2Bi3OdjIcqV3GSt69aivDnVew92wQdY%2Bt798eO5m9FthhVzkoSSMbNrqoGYbcO10%2FmSXoUIzmkfinSdIlad%2F%2FVZ0beTdv%2F%2BsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230412T173618Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAQAQMYILSVCRYH3RN%2F20230412%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=a5b08a45ef4f199210883aee9073263f9d5f7943d5c4037d99bcd2c249776604


Now, you can use this established connection to query your dataset as follows:

```sql
SELECT * FROM bgdataset.dataset.table LIMIT 10;
```
