using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000265: Bordeaux
/// </summary>
public class _11000265 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001082$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001084$
                // - The secrets of the Land of Darkness and Shadow Word cannot be explained by logic. Nature was not created by mathematics or science. They have a life all their own, which must be understood. 
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
