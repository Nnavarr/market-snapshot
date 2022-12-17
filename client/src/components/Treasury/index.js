const { Client } = require('pg');
const dotenv = require('dotenv');
dotenv.config();

const Treasury = () => {
  // connect to postgresql
  const connectDB = async () => {
      try {
          const client = new Client ({
            user: process.env.PGUSER,
            host: process.env.PGHOST,
            database: process.env.PGDATABASE,
            password: process.env.PGPASSWORD,
            port: process.env.PGPORT
          })

          await client.connect();

          const res = await client.query('SELECT * FROM treasury_rates');
          console.log(res);
          
          await client.end();
      }
      catch (error) {
        console.log(error)
      }
  }

  return (
    <h1> Hello World </h1>
  )
}

export default Treasury;


