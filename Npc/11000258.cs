using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000258: Hoon
/// </summary>
public class _11000258 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407001067$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001068$
                // - Please keep your voice down. I'm not supposed to be talking with anyone right now.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
