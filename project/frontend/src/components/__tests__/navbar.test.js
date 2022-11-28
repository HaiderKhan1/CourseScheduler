import Navbar from '../Navbar';
import { Link } from 'react-router-dom';
import { shallow } from 'enzyme';
import { SunIcon } from '@chakra-ui/icons';

describe('Navbar', () => {
  it('renders the navbar component without crashing', () => {
    shallow(<Navbar />);
  });

  // Check all the router links are there
  it('contains three links', () => {
    const wrapper = shallow(<Navbar />);
    const links = wrapper.find(Link);
    expect(links.length).toEqual(3);
  });

  // Check the links contain the correct paths
  it('links contain correct paths', () => {
    const wrapper = shallow(<Navbar />);
    const linksPaths = wrapper.find(Link).map((l) => l.props().to);
    expect(linksPaths).toEqual(['/', '/wiki', '/create-schedule']);
  });

  // Should have a sun icon when it's in dark mode
  it('has sun icon when its dark mode', () => {
    const wrapper = shallow(<Navbar />);
    const icon = wrapper.find(SunIcon).first();
    expect(icon.exists()).toBe(true);
  });
});
