import Navigation from "../navigation/Navigation";

interface Props {
  children: any;
}

export default function Layout({ children }: Props) {
  return (
    <div>
      <Navigation />
      <main>{children}</main>
    </div>
  );
}
