using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001607: Asimov
/// </summary>
public class _11001607 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006095$
    // - You're here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006144$
                // - We've joined forces under the banner of the Starlight Expedition. I only hope we can achieve what we've set out to do. 
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
