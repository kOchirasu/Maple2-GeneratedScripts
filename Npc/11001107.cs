using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001107: Vena
/// </summary>
public class _11001107 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003719$
    // - Mm... T-that's... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003722$
                // - Mom was right. She said anything can come true if I pray hard enough. I've prayed every day to be able to go back to her. Now I can!
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
