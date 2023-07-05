import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-handleproduct',
  templateUrl: './handleproduct.component.html',
  styleUrls: ['./handleproduct.component.css']
})
export class HandleproductComponent {


  Product: string = '';

  Description: string = '';
  Price: string = '';
  ProductImage: string = '';


  constructor(private http: HttpClient,private router: Router) { }

  onSubmit() {
    const data = {
      'Product': this.Product,
      'Description': this.Description,
      'Price': this.Price,
      'ProductImage':this.ProductImage
    };

    this.http.post('http://127.0.0.1:5000//addproducts', data).subscribe(response => {
      console.log(response);
      // handle success response here
    }, error => {
      console.error(error);
      // handle error response here
    });
    this.router.navigate(['/admin/items']);
  }



}
