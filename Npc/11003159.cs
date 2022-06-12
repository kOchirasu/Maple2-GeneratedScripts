using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003159: Beuti
/// </summary>
public class _11003159 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008059$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008062$
                // - I filled my backpack with flowers, and now I can smell them all the time! Oh, don't worry. They're not heavy at all.
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
