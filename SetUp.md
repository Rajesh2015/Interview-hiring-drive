# Interview-hiring-drive
This will help you setting up a fully functional **Spark Cluster** with **Spark Master**, **Spark Worker**, and **Jupyter Notebook** using Docker.

---

## **Prerequisites**

Before starting, make sure you have the following installed:

### **Step 0: Install Docker Desktop**

Download and install Docker Desktop:

* [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

### **Step 1: Install Git (if not already installed)**

Download from:

* [https://git-scm.com/install/](https://git-scm.com/install/)

---

## **Setup Instructions**


### **Step 1: Build & Start the Cluster**

Inside the project folder, run:

```
docker-compose down && docker-compose up -d --build
```

This will:

* Build the custom Jupyter + Spark image
* Start Spark Master, Spark Worker, and Jupyter Notebook

---

### **Step 2: Verify Containers Are Running**

Open **Docker Desktop** and go to **Containers**.
You should see the following running:

* `spark-master`
* `spark-worker`
* `jupyter`

---

### **Step 3: Submit a Spark Job**

To run `job.py`(This is something you will create and write your solution) inside the cluster, execute in vs code terminal:

```
docker exec -it spark-master /opt/spark/bin/spark-submit -com
```


---

## 🔵 **Optional Features**

### **1. Launch Jupyter Notebook with Spark**

Open the following link in your browser:

```
http://localhost:8888/lab?
```

You can now create notebooks that use Spark.

### **2. Adjust Spark Worker Memory**

If your system does not have enough RAM, you can lower memory allocation.

Edit `docker-compose.yml`:

```
SPARK_WORKER_MEMORY=8G
```

Set it to a smaller value if needed, for example:

```
SPARK_WORKER_MEMORY=4G
```
