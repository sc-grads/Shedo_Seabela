import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { HttpHeaders } from '@angular/common/http';
import { DomSanitizer } from '@angular/platform-browser';

interface product{

  ProductImage: string;
  Price: number;
  Description_re: string;
  ProductID: number;
  Product: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
products: product[] = [];


  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.http.get<any[]>('http://127.0.0.1:5000/items').subscribe(data => {
    this.products = data;


    });
  }

addToCart(ProductID: number): void {

  this.http.post<any>(`http://127.0.0.1:5000/AddToCart/${ProductID}`,ProductID)
    .subscribe(
        () => {
          alert('Product added to cart successfully');
          this.ngOnInit();
        },
      error => {
        console.error(error);
        // Handle error, show error message, etc.
      }
    );
}

}
