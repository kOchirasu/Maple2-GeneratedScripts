using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000977: Kunbasha
/// </summary>
public class _11000977 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003379$
    // - What's a human doing in a place like this?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003381$
                // - Only we kunkun can feel the flow of nature and foretell the weather. 
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
