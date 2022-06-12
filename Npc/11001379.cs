using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001379: Zenka
/// </summary>
public class _11001379 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005373$
    // - You called?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005376$
                // - Where in the world did they come from? Of course they chose <i>today</i> to cause a mess. When the dust clears, it'll be us security guards who take the fall for this.
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
