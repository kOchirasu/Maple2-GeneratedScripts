using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004464: Richmonde Defender
/// </summary>
public class _11004464 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012087$
    // - Huh? You don't look like a refugee.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012088$
                // - Huh? You don't look like a refugee.
                switch (selection) {
                    // $script:1227192907012089$
                    // - I have come from the distant land of Maple World.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012090$
                // - Never heard of it. Look, just keep your head down and try not to get caught in the crossfire.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
