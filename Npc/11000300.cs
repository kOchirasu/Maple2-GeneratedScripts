using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000300: Mills
/// </summary>
public class _11000300 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001191$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001193$
                // - Do you know what's living down below? $npcNamePlural:22000005$! They're so big and dreadful... Just looking at them leaves me petrified. How could I possibly get one of their tails?
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
