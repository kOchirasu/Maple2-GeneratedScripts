using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001520: Swordsman
/// </summary>
public class _11001520 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0515211707006107$
    // - Nice to meet you!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515211707006108$
                // - I'm honored to join the Starlight Expedition. The captain of the guard sent me to help $npc:11000076[gender:0]$. I intend to win glory for the guard!
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
