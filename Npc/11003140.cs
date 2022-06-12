using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003140: Jorge
/// </summary>
public class _11003140 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0222124707007951$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0224093607007961$
                // - Don't you just love the smell of my garden? My greatest joy is when I manage to reproduce extinct medicinal flowers. Heh... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
