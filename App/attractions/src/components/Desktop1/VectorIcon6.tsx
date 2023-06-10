import { memo, SVGProps } from 'react';

const VectorIcon6 = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 20 27' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <path
      d='M8.97229 26.4552C1.40469 15.3473 0 14.2073 0 10.125C0 4.5331 4.47714 0 10 0C15.5229 0 20 4.5331 20 10.125C20 14.2073 18.5953 15.3473 11.0277 26.4552C10.5311 27.1816 9.46885 27.1816 8.97229 26.4552ZM10 14.3437C12.3012 14.3437 14.1667 12.455 14.1667 10.125C14.1667 7.79504 12.3012 5.90625 10 5.90625C7.6988 5.90625 5.83333 7.79504 5.83333 10.125C5.83333 12.455 7.6988 14.3437 10 14.3437Z'
      fill='#FC5710'
    />
  </svg>
);
const Memo = memo(VectorIcon6);
export { Memo as VectorIcon6 };
