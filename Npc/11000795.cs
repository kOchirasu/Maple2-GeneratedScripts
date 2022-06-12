using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000795: Maritel
/// </summary>
public class _11000795 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002960$
    // - Welcome to Cathy Mart.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002961$
                // - Is there something you're looking for? You can find everything at Cathy Mart. If we don't have it, it doesn't exist!
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
