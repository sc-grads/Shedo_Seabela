import { Component } from '@angular/core';
import {  OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit {
  products: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getProducts();
  }

  getProducts() {
    this.http.get<any>('http://http://127.0.0.1:5000//products').subscribe(response => {
      this.products = response.products;
    }, error => {
      console.error(error);
    });
  }
}
