using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004214: Frontier Foundation Quartermaster
/// </summary>
public class _11004214 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806130507010732$
    // - Great work out there today!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806130507010733$
                // - I've got just what you need to continue the search.
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
