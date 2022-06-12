using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001055: Sansakova
/// </summary>
public class _11001055 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003606$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003607$
                // - No pizza can match Maggiore pizza. Chewy dough with simple toppings, just like Mom used to make! 
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
