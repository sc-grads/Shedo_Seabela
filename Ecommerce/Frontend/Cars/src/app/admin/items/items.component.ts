import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';
//
interface product{

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
  products: product[] = [];


  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.http.get<any[]>('http://127.0.0.1:5000/items').subscribe(data => {
    this.products = data;


    });
  }

deleteProduct(ProductID: number): void {

  this.http.delete<any>(`http://127.0.0.1:5000/deleteproducts/${ProductID}`)
    .subscribe(
        () => {
          alert('Product deleted successfully');
          this.ngOnInit();
        },
      error => {
        console.error(error);
        // Handle error, show error message, etc.
      }
    );
}

}
