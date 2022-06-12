using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001723: Vision
/// </summary>
public class _11001723 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006973$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507007025$
                // - I'm not telling you a thing. It's better that way.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
