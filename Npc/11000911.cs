using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000911: Manns
/// </summary>
public class _11000911 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003275$
    // - I don't want any questions.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003277$
                // - Please don't talk to me. I'm in the middle of doing the worst thing I can imagine.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
