using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000685: Einos
/// </summary>
public class _11000685 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002778$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002779$
                // - $map:02000227$ is the border between the mortal and spirit realms.
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
