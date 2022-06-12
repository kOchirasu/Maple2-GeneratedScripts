using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000328: Merjafar
/// </summary>
public class _11000328 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001333$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001335$
                // - People nowadays tend to throw their things away the moment they're done with them. It's a shame, really. 
                return 30;
            case (30, 1):
                // $script:0831180407001336$
                // - Antique items are precious relics of the past. You can trade antiques, but you can't bring the past back.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
