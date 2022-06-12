using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004196: Luanna
/// </summary>
public class _11004196 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010640$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010641$
                // - The world relies on the strength of heroes like you. May the empress's blessing be with you.
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
