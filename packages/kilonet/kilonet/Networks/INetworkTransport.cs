using System;
using System.IO;

namespace KBVE.Kilonet.Networks
{
  public interface INetworkTransport
  {
    void Connect(string serverUri, ushort port);
    void Send(byte[] data);
    void Send(Stream dataStream);
    void Receive(Action<byte[]> onReceive);
    void Receive(Action<Stream> onReceiveStream);
    void Disconnect();
    void Update();
  }
}
