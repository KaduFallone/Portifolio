import { Component, inject } from '@angular/core';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ProductsService } from '../../shared/services/products.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { Product } from '../../shared/interfaces/product.interface';
import { FormComponent } from '../../shared/components/form/form.component';
import { MatCardModule } from '@angular/material/card';
import { BackToListComponent } from "../../shared/components/back-to-list/back-to-list.component";

@Component({
  selector: 'app-edit',
  standalone: true,
  imports: [FormComponent, MatButtonModule, MatCardModule, BackToListComponent],
  templateUrl: './edit.component.html',
  styleUrl: './edit.component.scss'
})
export class EditComponent {

  productService = inject(ProductsService);
  matSnackBar = inject(MatSnackBar)
  router = inject(Router);

  product: Product = inject(ActivatedRoute).snapshot.data['product'];
  
  onSubmit(product: Product){
    this.productService.put(this.product.id, product).subscribe(() => {
      this.matSnackBar.open('Produto editado com sucesso!!', 'Okay')

      this.router.navigateByUrl('/')
    });
  }

}
