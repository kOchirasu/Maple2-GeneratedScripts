using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001555: Valen
/// </summary>
public class _11001555 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0415104107006021$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0421104907006047$
                // - Tsk. If people keep taking pebbles home as souvenirs, soon the beach will be completely bare.
                return 40;
            case (40, 1):
                // $script:0421104907006048$
                // - This one time, somebody climbed the hill in the middle of the night to get up close to the whale. Or he tried to, but he lost his grip halfway up and fell. It was a total disaster.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
