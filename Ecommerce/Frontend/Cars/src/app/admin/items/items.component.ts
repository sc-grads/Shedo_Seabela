import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';

interface Product {
  ProductImage: string;
  Price: number;
  Description_re: string;
  ProductID: number;
  Product: string;
}

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit {
  products: Product[] = [];


  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.http.get<any[]>('http://127.0.0.1:5000/items').subscribe(data => {
    console.log(data);
      this.products = data;
    });
  }
//   getProducts() {
//   const headers = new HttpHeaders().set('Content-Type', 'application/json');
//     this.http.get('http://127.0.0.1:5000/items', { headers }).subscribe(response => {
//      // this.products = response.products
//       console.log(response);
//       console.log("hello world")
//     }, error => {
//       console.error(error);
//     });

}
