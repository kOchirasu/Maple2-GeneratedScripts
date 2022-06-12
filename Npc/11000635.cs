using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000635: Prisoner 140918
/// </summary>
public class _11000635 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002582$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002585$
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:0831180407002586$
                    // - How did you end up in here?
                    case 0:
                        return 31;
                }
                return 30;
            case (30, 1):
                // $script:0831180407002588$
                // - Ugh... This smell... The toilet is clogged...
                return -1;
            case (31, 0):
                // $script:0831180407002587$
                // - For swearing. Why? Don't say you never swear. Everyone does it! So why is it such a crime??
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (30, 1) => NpcTalkButton.Close,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
