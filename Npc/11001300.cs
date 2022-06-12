using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001300: Allon
/// </summary>
public class _11001300 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1215203907005014$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1215203907005017$
                // - I command the Royal Knights of Empress $npcName:11000075[gender:1]$. Her safety is our duty.
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
