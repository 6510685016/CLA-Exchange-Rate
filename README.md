# Command Line Application 
*This project is a COPY of my group project on GitHub Classroom.

## Overview 
This project is a command-line application built with Python, using the Alpha Vantage API to fetch financial data. It allows users to retrieve exchange rates data, such as daily, weekly, or monthly rates, and view the supported currencies. The application is containerized using Docker.

## Command 
  - **cli-exc help** - display available subcommands/options
  - **cli-exc list [OPTIONS]** - display supported currencies
  - **cli-exc realtime** (from_currency) (to_currency) (amount) - fetch realtime exchange rates
  - **cli-exc daily** (from_currency) (to_currency) (date) (amount) - fetch daily exchange rates
  - **cli-exc weekly** (from_currency) (to_currency) (week) (amount) - fetch weekly exchange rates
  - **cli-exc monthly** (from_currency) (to_currency) (month) (amount) - fetch monthly exchange rates
  - **cli-exc max_min** (period) (from_currency) (to_currency) - fetch maximum rates and minimum rates for last 7 days or last 30 days
  - **cli-exc volatile** (period) (from_currency) (to_currency) - fetch volatile for last 7 days or last 30 days
    
  
## Setup 
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/cn330/g01-67_01.git G01_CLA
   cd G01_CLA
   ```

2. **Create and Activate a Virtual Environment:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  
   ```

   On Windows use
   ```sh
   .venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install the Application in Editable Mode:**
   ```sh
   pip install -e .
   ```

5. **Using the Application:**
   - To check available commands, run:
     ```sh
     cli-exc help
     cli-exc list
     ```
   - To fetch the exchange rates Realtime, use:
  
      Options:
         --money TEXT  จำนวนเงินที่ต้องการแปลง [default: 1.0]

     ```sh
     cli-exc realtime FROM_CURRENCY TO_CURRENCY [OPTIONS]
   
   - e.g. convert 100 USD to THB using real-time exchange rates
      ```
      cli-exc realtime usd thb --money 100
      ```
     
   - To fetch the exchange rates for a specific period, use:
  
      Options: -a, --amount FLOAT  จำนวนเงินที่ต้องการแปลง -c, --convert       แปลงสกุลเงิน

      DATE format: [YYYY-MM-DD] 
      
      MONTH format: [YYYY-MM]

     ```sh
     cli-exc monthly [OPTIONS] FROM_CURRENCY TO_CURRENCY [MONTH]
     cli-exc weekly [OPTIONS] FROM_CURRENCY TO_CURRENCY [DATE]
     cli-exc daily [OPTIONS] FROM_CURRENCY TO_CURRENCY [DATE]
     ```
   - e.g. convert 100 USD to THB using monthly exchange rates
      ```
      cli-exc monthly usd thb 2024-11 --convert --amount 100
      ```
   - To fetch maximum rates and minimum rates for last 7 days or last 30 days
      ```
      cli-exc max_min PERIOD CURRENCY_FROM CURRENCY_TO
      ```
   - e.g. fetch maximum rates and minimum rates for last 7 days
      ```
      cli-exc max_min last7 usd thb
      ```
   - To fetch volatile for last 7 days or last 30 days
      ```
      cli-exc volatile PERIOD CURRENCY_FROM CURRENCY_TO
      ```
   - e.g. fetch volatile for last 7 days
      ```
      cli-exc volatile last7 usd thb
      ```

## Docker Setup
The application is containerized with Docker. You can use Docker Compose to run it in a containerized environment. 

Remark : Please use command prompt to run the appllication.

1. **Build and Run with Docker Compose:**
   ```sh
   docker-compose up --detach
   ```

2. **To enter a Docker container in interactive mode:**
   ```
   docker exec -it g01-67_01 /bin/bash
   ```   
