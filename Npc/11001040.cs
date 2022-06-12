using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001040: Fordson
/// </summary>
public class _11001040 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003552$
    // - The wind is so cold.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003555$
                // - Maritime Leaguers are atmospheric, oceanic, and geologic specialists gathered to observe and collect information about the oceans and everything in it.
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
