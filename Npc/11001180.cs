using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001180: Mayar
/// </summary>
public class _11001180 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1110150406000967$
    // - Ooh... Everything here is so interesting!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1110150406000970$
                // - This place seems so peaceful. And everyone has such strange clothes! What's that person eating? I have so many questions!
                return 30;
            case (30, 1):
                // $script:1110150406000971$
                // - ...Ah! Yalario! Are you from around here? It is nice to meet you.
                switch (selection) {
                    // $script:1110150406000972$
                    // - Yala-what-io?
                    case 0:
                        return 31;
                    // $script:1110150406000973$
                    // - You sure have a lot of questions.
                    case 1:
                        return 32;
                    // $script:1110150406000974$
                    // - Where exactly are you from?
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1110150406000975$
                // - Hehe... Yalario is a greeting in my language. It means <b>awaited stranger</b>! Although, the literal translation is more like "well-groomed beard."
                return -1;
            case (32, 0):
                // $script:1110150406000976$
                // - How could I not? Visiting a new place is so exciting! I can't wait to learn more about this land and its people.
                return 32;
            case (32, 1):
                // $script:1110150406000977$
                // - There are so many different types of people here! You must have lots of festivals and holidays of your own. I can't wait to see them!
                return -1;
            case (33, 0):
                // $script:1110150406000978$
                // - Mm... It is a distant land. You probably haven't heard of it. We traveled a great distance by ship to get here. Our village was not at all like this Town of Queens.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
