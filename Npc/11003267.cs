using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003267: Allon
/// </summary>
public class _11003267 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008214$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008217$
                // - I am captain of the Royal Guard. Each and every one of my men would lay down his life in service to Empress $npcName:11000075[gender:1]$.
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
