using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000244: Mrs. Toulette
/// </summary>
public class _11000244 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407001037$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001041$
                // - Why are you talking to me? What do you want?
                return -1;
            case (50, 0):
                // $script:0831180407001042$
                // - People say that the richer you get, the pickier you get. Makes sense, since you can have whatever you want with enough money.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
