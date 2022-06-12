using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000462: Amelia
/// </summary>
public class _11000462 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002052$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002056$
                // - What brings you to $map:02000107$? Since you're here, I was thinking about changing up my skin tone again. Do you think I should do it?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
