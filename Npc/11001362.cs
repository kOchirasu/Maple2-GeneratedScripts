using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001362: Startz
/// </summary>
public class _11001362 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215222907005045$
    // - No one toys with my people and gets away with it.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005711$
                // - You saved us all, but I'm not going to thank you twice.
                return 40;
            case (40, 1):
                // $script:1227194507005712$
                // - <i>Maybe</i> I'll treat you to a meal.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
