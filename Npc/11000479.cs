using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000479: Hameron
/// </summary>
public class _11000479 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002096$
    // - Do, mi, so, do! How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002099$
                // - As a musician, I want to make music from the most beautiful tones of nature. That's my dream.
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
