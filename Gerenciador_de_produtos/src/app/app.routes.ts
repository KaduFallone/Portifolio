import { ListComponent } from './features/list/list.component';
import { Routes } from '@angular/router';
import { getProducts, } from './shared/resolvers/get-products.resolver';
import { getId } from './shared/resolvers/edit-product.resolver';

export const routes: Routes = [{
    path: '',
    resolve:{
        products: getProducts
    },
    component: ListComponent, 
},
{
    path: 'create-product',
    loadComponent: () => 
        import('./features/create/create.component').then( 
            (m) => m.CreateComponent
        ),
},
{
    path: 'edit-product/:id',
    resolve: {
        product: getId
    },
    loadComponent: () => 
        import('./features/edit/edit.component').then((m) => m.EditComponent),
},

];
