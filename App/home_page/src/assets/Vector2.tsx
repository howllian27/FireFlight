export default function Vector2(props: Vector2Props) {
  return (
    <div className={`${props.className}`}>
      <svg
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        viewBox="0 0 54 47"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 1.688 10.071 H 45.563 C 46.495 10.071 47.25 9.32 47.25 8.393 V 1.679 C 47.25 0.751 46.495 0 45.563 0 H 1.688 C 0.755 0 0 0.751 0 1.679 V 8.393 C 0 9.32 0.755 10.071 1.688 10.071 Z M 52.313 18.464 H 8.438 C 7.505 18.464 6.75 19.215 6.75 20.143 V 26.857 C 6.75 27.785 7.505 28.536 8.438 28.536 H 52.313 C 53.245 28.536 54 27.785 54 26.857 V 20.143 C 54 19.215 53.245 18.464 52.313 18.464 Z M 45.563 36.929 H 1.688 C 0.755 36.929 0 37.68 0 38.607 V 45.321 C 0 46.249 0.755 47 1.688 47 H 45.563 C 46.495 47 47.25 46.249 47.25 45.321 V 38.607 C 47.25 37.68 46.495 36.929 45.563 36.929 Z"
          fill="black"
         />
      </svg>
    </div>
  );
}

Vector2.defaultProps = {
  className: "",
};

interface Vector2Props {
  className: string;
}

/**
 * This component was generated from Figma with FireJet.
 * Learn more at https://www.firejet.io
 *
 * README:
 * The output code may look slightly different when copied to your codebase. To fix this:
 * 1. Include the necessary fonts. The required fonts are imported from public/index.html
 * 2. Include the global styles. They can be found in App.css
 *
 * Note: Step 2 is not required for tailwind.css output
 */
