 import React from 'react'

 import { Chart as ChartJS, defaults } from "chart.js/auto";
 import { Bar, Doughnut, Line } from "react-chartjs-2";
import Navbar from './MyNavbar';
import NavbarComponent from './MyNavbar';

 
 
 const data = {
    labels: ['January', 'February', 'March', 'April', 'May'],
    datasets: [{
      label: 'Monthly Sales',
      data: [12, 19, 3, 5, 2],
      fill: false,
      borderColor: 'rgba(75, 192, 192, 1)',
      tension: 0.1,
    }],
}


 const ChartComponent = () => {
    
   return (
     <>
        <Line data ={data} />
     </>
   )
 }
 
 export default ChartComponent