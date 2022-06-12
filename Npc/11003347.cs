using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003347: Ralph's Lackey
/// </summary>
public class _11003347 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0517164307008490$
    // - I've never met someone as strong as you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0517164307008493$
                // - I can take you to the boss if you're lost.
                switch (selection) {
                    // $script:0517164307008494$
                    // - Lead the way.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0517164307008495$
                // - Sure thing. Right this way.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
