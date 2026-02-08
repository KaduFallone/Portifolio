import { Component, inject } from '@angular/core';
import { ProductsService } from '../../shared/services/products.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { FormComponent } from '../../shared/components/form/form.component';
import { Product } from '../../shared/interfaces/product.interface';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { BackToListComponent } from "../../shared/components/back-to-list/back-to-list.component";

@Component({
  selector: 'app-create',
  standalone: true,
  imports: [FormComponent, MatButtonModule, MatCardModule, BackToListComponent],
  templateUrl: './create.component.html',
  styleUrl: './create.component.scss',
})
export class CreateComponent {

  productService = inject(ProductsService);
  matSnackBar = inject(MatSnackBar);
  router = inject(Router);

  product: Product = inject(ActivatedRoute).snapshot.data['product'];

  onSubmit(product: Product){
    this.productService.post(product).subscribe(() => {
      this.matSnackBar.open('Produto criado com sucesso!!', 'Okay');

      this.router.navigateByUrl('/');
    });
  }
}
